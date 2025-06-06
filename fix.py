import os
import nbformat

def fix_widget_metadata(nb_path):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    widgets = nb.metadata.get("widgets", {})
    widget_json = widgets.get("application/vnd.jupyter.widget-state+json", {})

    if "state" not in widget_json and any(isinstance(v, dict) and "state" in v for v in widget_json.values()):
        print(f"🔧 Repairing widget metadata in Folder: {nb_path}")
        new_state = {
            "state": widget_json,
            "version_major": 2,
            "version_minor": 0
        }
        nb.metadata["widgets"]["application/vnd.jupyter.widget-state+json"] = new_state

        fixed_path = nb_path.replace(".ipynb", "_fixed.ipynb")
        with open(fixed_path, "w", encoding='utf-8') as f:
            nbformat.write(nb, f)
    else:
        print(f"✅ Normal: {nb_path}")

def walk_and_fix(root_dir):
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".ipynb") and not file.endswith("_fixed.ipynb"):
                fix_widget_metadata(os.path.join(root, file))

if __name__ == "__main__":
    target_dir = input("📂 Enter the directory path to fix widget metadata: ").strip()
    walk_and_fix(target_dir)
    print("🎉 Work Done.")
