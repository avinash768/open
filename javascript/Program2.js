const array = [1, 5, 3, 4, 2];

for (let i = 0; i < array.length - 1; i++) {
  for (let j = i + 1; j < array.length; j++) {
    if (array[i] < array[j]) {
      let temp = array[i];
      array[i] = array[j];
      array[j] = temp;
    }
  }
}

console.log(array); 
