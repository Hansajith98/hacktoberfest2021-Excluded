/**
 * This function checks if two strings are anagrams
 */

const checkAnagram = (first, second) => {
    
    if (first.length !== second.length) {
        return false;
    }

    const letterList = {};

    for (let i = 0; i < first.length; i++) {
        let letterCount = first[i];

        if (letterList[letterCount]) {
            letterList[letterCount]++;
        } else {
            letterList[letterCount] = 1;
        }
    }
    
    for (let i = 0; i < second.length; i++) {
        let letterCount = second[i];

        if (!letterList[letterCount]) {
            return false;
        } else {
            letterList[letterCount]--;
        }
    }
    
      return true;
}
;

console.log(checkAnagram("anagram", "margana")); // true
console.log(checkAnagram("anagrama", "margani")); // false
 