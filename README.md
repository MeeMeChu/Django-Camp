# Django-Camp

ระบบเพิ่มรายชื่อนักศึกษาหรือนักเรียน ในรูปแบบตาราง

# Get Stated

```bash
pipenv install
pipenv shell
python manage.py runserver
```

# Install Sweetify - SweetAlert2 for Django

```bash
pipenv install sweetify
```

**เพิ่มลงใน Django**

```python
INSTALLED_APPS = [
    ...
    'sweetify'
]

# possible options: 'sweetalert', 'sweetalert2' - default is 'sweetalert2'
SWEETIFY_SWEETALERT_LIBRARY = 'sweetalert2'
```

**เพิ่มลงในไฟล์ templates**

```jinja
...

{% load sweetify %}
{% sweetify %}
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>

</body>
</html>
```

**ทดสอบใช้งานว่าสามารถใช้งานได้หรือไม่?**

```python
sweetify.success(request, 'คุณกรอกข้อมูลสำเร็จ', text='เราได้บันทึกข้อมูลของคุณแล้ว!', persistent='OK!')

sweetify.error(request, 'เกิดข้อผิดพลาด', text='คุณกรอกข้อมูลไม่ครบหรือชื่อซ้ำกัน', persistent='OK!')
```

REF : (https://github.com/Atrox/sweetify-django/tree/master),
(https://sweetalert2.github.io)
