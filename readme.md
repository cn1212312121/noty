cn1212312121


# build image
docker build -t etm-noty .

# รัน โดยดึงค่าจาก .env ไฟล์ตรงๆ
docker run -d --name etm-noty --env-file .env --restart unless-stopped etm-noty


# ดู log แบบ real-time
docker logs -f etm-noty

# หยุด/ลบ container
docker stop etm-noty && docker rm etm-noty

# รีบิลด์ใหม่หลังแก้โค้ด แล้วรันใหม่
docker stop etm-noty && docker rm etm-noty
docker build -t etm-noty .
docker run -d --name etm-noty --env-file .env --restart unless-stopped etm-noty


docker build -t etm-noty . && docker run -d --name etm-noty --env-file .env --restart unless-stopped etm-noty


#run ใหม่
docker stop etm-noty 2>/dev/null; docker rm etm-noty 2>/dev/null; docker build -t etm-noty . && docker run -d --name etm-noty --env-file .env --restart unless-stopped etm-noty
