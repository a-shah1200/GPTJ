FROM python:3.10.17-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    portaudio19-dev \
    libasound-dev \
    libportaudio2 \
    libportaudiocpp0 \
    ffmpeg \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .


RUN pip3 install --no-cache-dir -r requirements.txt



WORKDIR /app

COPY . .



EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
