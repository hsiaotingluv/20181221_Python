// // Method 1
// function fib(n) {
//     return n <= 1 ? n : fib(n - 1) + fib(n - 2);
// }

// fib(3)

// // Method 2

// function f(n, k, f_k_minus_2, f_k_minus_1) {
//     return (k > n) ? f_k_minus_1 : f(n, k + 1, f_k_minus_1, f_k_minus_2 + f_k_minus_1);
// }

// function fib(n) {
//     return (n < 2) ? n : f(n, 2, 0, 1);
// }

// fib(3)


// Greatest commom divisor

function gcd(a, b) {
    return a === b ? a : a > b ? gcd(a - b, b) : gcd(a, b - a);
}

gcd(10, 5)