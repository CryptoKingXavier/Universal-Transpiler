public class Calculator {
  public static float add(float num1, float num2) { return num1 + num2; }
  public static float subtract(float num1, float num2) { return num1 - num2; }
  public static float multiply(float num1, float num2) { return num1 * num2; }
  public static float divide(float num1, float num2) {
    if (num2 == 0) {
      return 0;
    } else {
      return num1 / num2;
    }
  }

  public static void main(String[] args) {
    System.out.println(add(3, 4));
    System.out.println(subtract(3, 4));
    System.out.println(multiply(3, 4));
    System.out.println(divide(3, 4));
  }
}