
abstract class Geometric_Shape
{
    public abstract double GetArea(); // абстрактный метод для получения площади
    public override string ToString() 
    {
        return $"Площадь: {GetArea()}";
    }
}
class Rectangle: Geometric_Shape
{
    private double width_ { get; set; }
    private double height_ { get; set; }
    public Rectangle(int width, int height)
    {
        width_ = width;
        height_ = height;
    }
    public override double GetArea() => width_ * height_; // переопрелеление получения площади
    public void Print()
    {
        Console.WriteLine($"Треугольник: Ширина = {width_}, Высота = {height_}. {ToString()}");
    }
}
class Squaree : Geometric_Shape
{
    private double side_ { get; set; }
    public Squaree(int side)
    {
        side_ = side;
    }
    public override double GetArea() => Math.Pow(side_, 2); // переопрелеление получения площади
    public void Print()
    {
        Console.WriteLine($"Квадрат: Сторона = {side_}. {ToString()}");
    }
}
class Circle : Geometric_Shape
{
    private double radius_ { get; set; }
    public Circle(int radius)
    {
        radius_ = radius;
    }
    public override double GetArea() => Math.PI * Math.Pow(radius_, 2); // переопрелеление получения площади
    public void Print()
    {
        Console.WriteLine($"Круг: Радиус = {radius_}. {ToString()}");
    }
}
class Program
{
    static void Main(string[] args)
    {
        Rectangle rectangle = new Rectangle(5, 10); // Создание объекта прямоугольник
        rectangle.Print();

        Squaree squaree = new Squaree(5); // Создание объекта квадрат
        squaree.Print();

        Circle circle = new Circle(10); // Создание объекта прямоугольника
        circle.Print();
    }
}