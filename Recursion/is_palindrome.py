def is_palindrome(lst, start, end):
    if start >= end:
        return True
    if lst[start] != lst[end]:
        return False
    return is_palindrome(lst, start+1, end-1)

lst = [1, 2, 3, 4, 4, 2, 1]
print(is_palindrome(lst, 0, len(lst)-1))





# # Java
# public class Palindrome {
#     public static boolean isPalindromeRecursive(int[] array, int start, int end) {
#         if (start >= end) {
#             return true;
#         }
#         if (array[start] != array[end]) {
#             return false;
#         }
#         return isPalindromeRecursive(array, start + 1, end - 1);
#     }
#
#     public static void main(String[] args) {
#         int[] array = {1, 2, 3, 2, 1};
#         System.out.println("Is Palindrome: " + isPalindromeRecursive(array, 0, array.length - 1));
#     }
# }
#
#
#
#
# C#
# using
# System;
# class Program
#     {
#         static bool IsPalindromeRecursive(int[] array, int start, int end)
#     {
#     if (start >= end)
#         return true;
#
#     if (array[start] != array[end])
#         return false;
#
#     return IsPalindromeRecursive(array, start + 1, end - 1);
#     }
#
# static void Main(string[] args)
#  {
# int[]
#     array = {1, 2, 3, 2, 1};
#     Console.WriteLine("Is Palindrome: " + IsPalindromeRecursive(array, 0, array.Length - 1));
#  }
# }
#
#
# # cpp
# #include <iostream>
# using namespace std;
#
# bool isPalindromeRecursive(int array[], int start, int end) {
#     if (start >= end) {
#         return true;
#     }
#     if (array[start] != array[end]) {
#         return false;
#     }
#     // بازگشت برای زیرمسئله
#     return isPalindromeRecursive(array, start + 1, end - 1);
# }
#
# int main() {
#     int array[] = {1, 2, 3, 2, 1};
#     int size = sizeof(array) / sizeof(array[0]);
#     cout << "Is Palindrome: " << (isPalindromeRecursive(array, 0, size - 1) ? "true" : "false") << endl;
#     return 0;
# }
#
#
#
# #JavaScript
# function isPalindromeRecursive(array, start, end) {
#     if (start >= end) {
#         return true;
#     }
#     if (array[start] !== array[end]) {
#         return false;
#     }
#     return isPalindromeRecursive(array, start + 1, end - 1);
# }
#
# const array = [1, 2, 3, 2, 1];
# console.log("Is Palindrome:", isPalindromeRecursive(array, 0, array.length - 1));
#
#
#
# #PHP
# <?php
# function isPalindromeRecursive($array, $start, $end) {
#     if ($start >= $end) {
#         return true;
#     }
#     if ($array[$start] != $array[$end]) {
#         return false;
#     }
#     return isPalindromeRecursive($array, $start + 1, $end - 1);
# }
#
# $array = [1, 2, 3, 2, 1];
# echo "Is Palindrome: " . (isPalindromeRecursive($array, 0, count($array) - 1) ? "true" : "false");
# ?>
