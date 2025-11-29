# file: deployment.py
import modal

image = (
    modal.Image.debian_slim()
    .pip_install(["uv"])
    .add_local_file("demo.py", "/app/demo.py", copy=True)
    .add_local_dir("layouts", "/app/layouts", copy=True)
    .workdir("/app")
)

app = modal.App(name="marimo-app")


@app.function(image=image, allow_concurrent_inputs=100)
@modal.web_server(8000, startup_timeout=60)
def marimo_app():
    print("Hello, World!")
    import subprocess

    # Port must match the web_server port, and host must be 0.0.0.0 for this to work.
    cmd = "uvx marimo run demo.py --sandbox --port 8000 --host 0.0.0.0 --headless"
    subprocess.Popen(cmd, shell=True)
