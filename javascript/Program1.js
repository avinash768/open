function reverseWords(sentence) {
    return sentence.split(" ").map(word => word.split("").reverse().join(""));
  }
  
  // Example usage:
  const sentence = "This is a sunny day";
  const reversedSentence = reverseWords(sentence);
  
  console.log(reversedSentence); // "shiT si a ynnus yad"
  