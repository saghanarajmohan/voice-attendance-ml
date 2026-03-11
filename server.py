from flask import Flask, request
import os

app = Flask(__name__)

DATASET_PATH = "DATASET"

if not os.path.exists(DATASET_PATH):
    os.makedirs(DATASET_PATH)

@app.route("/")
def home():
    return "Voice Attendance Server Running"

@app.route("/upload", methods=["POST"])
def upload():

    name = request.args.get("name")

    if not name:
        return "Name missing", 400

    user_folder = os.path.join(DATASET_PATH, name)

    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    count = len(os.listdir(user_folder)) + 1

    file_path = os.path.join(user_folder, f"{count}.wav")

    with open(file_path, "wb") as f:
        f.write(request.data)

    return "Audio Saved"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
