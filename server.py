"""
1409 SDK — Flask Dev Server + Admin Panel
"""

from flask import Flask, render_template, jsonify, abort, request  # noqa: F401
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# ── CORS — allow any origin to load SDK assets ──────────────────────────────

@app.after_request
def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# ── Paths ──────────────────────────────────────────────────────────────────
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR    = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
COMPONENTS_DIR = os.path.join(TEMPLATES_DIR, "components")

# ── Helper ─────────────────────────────────────────────────────────────────

def list_files(directory, extensions=None):
    """Return sorted list of files in a directory, optionally filtered."""
    result = []
    for root, _, files in os.walk(directory):
        for f in sorted(files):
            if extensions and not any(f.endswith(e) for e in extensions):
                continue
            rel = os.path.relpath(os.path.join(root, f), BASE_DIR)
            result.append(rel.replace("\\", "/"))
    return result


# ── Main pages ─────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("admin/index.html",
                           css_files=list_files(STATIC_DIR, [".css"]),
                           html_files=list_files(COMPONENTS_DIR, [".html"]),
                           static_files=list_files(STATIC_DIR,
                               [".png", ".svg", ".jpg", ".ttf", ".gif"]))


@app.route("/preview/<path:component>")
def preview(component):
    """Render a component template in a preview iframe."""
    allowed = list_files(COMPONENTS_DIR, [".html"])
    allowed_names = [os.path.basename(p) for p in allowed]
    if component not in allowed_names:
        abort(404)

    component_path = os.path.join(COMPONENTS_DIR, component)
    with open(component_path, "r", encoding="utf-8") as f:
        source = f.read()

    # Full-page templates (extend base) are rendered directly
    if "{% extends" in source:
        return render_template(f"components/{component}")

    # Snippets get wrapped in a preview shell so CSS/Lucide are available
    return render_template("preview_shell.html",
                           component_html=source,
                           component_name=component)


# ── API: file list ─────────────────────────────────────────────────────────

@app.route("/api/files")
def api_files():
    return jsonify({
        "css":        list_files(STATIC_DIR, [".css"]),
        "components": list_files(COMPONENTS_DIR, [".html"]),
        "static":     list_files(STATIC_DIR,
                          [".png", ".svg", ".jpg", ".ttf", ".gif"])
    })


@app.route("/api/file-content")
def api_file_content():
    path = request.args.get("path", "")
    full = os.path.normpath(os.path.join(BASE_DIR, path))
    if not full.startswith(BASE_DIR):
        abort(403)
    if not os.path.isfile(full):
        abort(404)
    with open(full, "r", encoding="utf-8") as f:
        return jsonify({"content": f.read()})


# ── Run ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("1409 SDK Admin Server → http://localhost:5055")
    app.run(debug=True, port=5055)
