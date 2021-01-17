function validAnagram(firstStr, secondStr) {
    if (firstStr.length !== secondStr.length) {
        return false
    };
    const lookup = {};

    for (let i = 0; i < firstStr.length; i++) {
        let letter = firstStr[i];
        lookup[letter] ? lookup[letter] += 1 : lookup[letter] = 1;
    };
    for (let i = 0; i < secondStr.length; i++) {
        let letter = secondStr[i];
        if (!lookup[letter]) {
            return false;
        } else {
        lookup[letter] -= 1;
        }
    };
    return true;
};


validAnagram('anagram', 'nagaram');