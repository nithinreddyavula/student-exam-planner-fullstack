FROM python:3.11-slim
WORKDIR /app
ENV PIP_NO_CACHE_DIR=1
ENV TORCH_CUDA_ARCH_LIST=""
ENV CUDA_VISIBLE_DEVICES=""
RUN pip install torch --index-url https://download.pytorch.org/whl/cpu
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
