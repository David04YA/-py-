# 基于类创建对象，使用对象的属性和行为，来完成功能开发,就是面向对象编程

class Clock:
    id=None
    price=None
    brand=None
    

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 构建两个Clock对象并让其工作
c1=Clock()
c1.id=1
c1.price=100
c1.brand="中国"
c1.ring()

