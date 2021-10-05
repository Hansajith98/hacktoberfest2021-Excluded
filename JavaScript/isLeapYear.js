/**
 * The function tells you if the year is a leap year or a common year
 * The function takes an integer as argument
 */

const isLeapYear = (year) => {
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
        console.log(`${year} is leap year`);
    } else {
        console.log(`${year} is common year`);
    }
}

isLeapYear(1600); // leap year
isLeapYear(1990); // common year
isLeapYear(2016); // leap year
isLeapYear(2021); // common year
isLeapYear(2400); // leap year
isLeapYear(2100); // common year