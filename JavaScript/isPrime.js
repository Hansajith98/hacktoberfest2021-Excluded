/**
 * The function tells if the number is prime
 * The function takes an integer as an argument
 */

const isPrime = (num) => {
    let i = 2;
    let result = true;

    while (i <= num / 2) {
        if (num % i != 0) {
            i = i + 1
        } else {
            result = false;
            break;
        }
    }
    
    if (result) {
        console.log(`${num} is a prime number`);
    } else {
        console.log(`${num} is not a prime number`);
    }
}

isPrime(5) // prime
isPrime(15) // isn't prime
isPrime(23) // prime