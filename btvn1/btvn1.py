from fastapi import FastAPI

app = FastAPI()
students = [
    "An",
    "Binh",
    "Cuong"
]

@app.get("/students")
def get_students():
    return {
        "message": "Lấy danh sách sinh viên thành công",
        "data": students
    }
# 1. Trace luồng xử lý khi gọi /getStudents:
# Khi client gửi request đến /getStudents, FastAPI gọi hàm xử lý và trả kết quả về cho client dưới dạng response.

# 2. Vì sao không nên trả về string trong API JSON:
# Vì frontend mong nhận dữ liệu JSON để xử lý, còn string chỉ là văn bản nên không đúng chuẩn REST API.

# 3. Lỗi trong thiết kế REST endpoint (naming convention):
# Endpoint /getStudents không đúng chuẩn REST vì chứa động từ get; nên đặt là /students để biểu diễn tài nguyên.