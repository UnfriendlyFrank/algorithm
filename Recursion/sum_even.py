def sum_even(n):
    if n<=0:
        return 0
    elif n %2 != 0:
        return sum_even(n-1)
    else:
        return n + sum_even(n-2)

print(sum_even(10))



# -----------java-----------
# public class SumEven {
#     public static int sumEven(int n) {
#         if (n <= 0) {
#             return 0;
#         } else if (n % 2 != 0) {
#             return sumEven(n - 1);
#         } else {
#             return n + sumEven(n - 2);
#         }
#     }
#
#     public static void main(String[] args) {
#         System.out.println(sumEven(8)); // : 20
#     }
# }


# -----------C#-----------
# using System;
# class Program {
#     static int SumEven(int n) {
#         if (n <= 0) {
#             return 0;
#         } else if (n % 2 != 0) {
#             return SumEven(n - 1);
#         } else {
#             return n + SumEven(n - 2);
#         }
#     }
#
#     static void Main() {
#         Console.WriteLine(SumEven(8)); // : 20
#     }
# }


# -----------javascript-----------
# function sumEven(n) {
#     if (n <= 0) {
#         return 0;
#     } else if (n % 2 !== 0) {
#         return sumEven(n - 1);
#     } else {
#         return n + sumEven(n - 2);
#     }
# }
#
# console.log(sumEven(8)); // : 20


# -----------c++----------
# include <iostream>
# int sumEven(int n) {
#     if (n <= 0) {
#         return 0;
#     } else if (n % 2 != 0) {
#         return sumEven(n - 1);
#     } else {
#         return n + sumEven(n - 2);
#     }
# }
#
# int main() {
#     std::cout << sumEven(8) << std::endl; // خروجی: 20
#     return 0;
# }

