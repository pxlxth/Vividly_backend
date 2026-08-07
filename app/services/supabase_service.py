import os
from pathlib import Path

from dotenv import load_dotenv
from supabase import Client, create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

BASE_DIR = Path(__file__).resolve().parents[2]

def download_video(bucket: str, remote_path: str, local_path: str):

    output_path = BASE_DIR / local_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    data = supabase.storage.from_(bucket).download(remote_path)

    with open(output_path, "wb") as file:
        file.write(data)

    return str(output_path)

def get_lesson_by_id(lesson_id: str):
    response = (
        supabase.table("lessons")
        .select("*")
        .eq("id", lesson_id)
        .single()
        .execute()
    )

    return response.data