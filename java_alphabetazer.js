var moonWalkers = [
  "Neil Armstrong",
  "Buzz Aldrin",
  "Pete Conrad",
  "Alan Bean",
  "Alan Shepard",
  "Edgar Mitchell",
  "David Scott",
  "James Irwin",
  "John Young",
  "Charles Duke",
  "Eugene Cernan",
  "Harrison Schmitt"
];

function turn_name(string){
    var new_name = string.split(" ")[1] + " " + string.split(" ")[0];
    return new_name;
}

function alphabetizer(names) {
    var new_list = []
    for (var name in names){
        new_name = turn_name(names[name]);
        new_list.push(new_name);
    }
    var sorted = new_list.sort();
    var result = []
    for (var name1 in sorted){
        result.push(turn_name(sorted[name1]));
    }
    return [names, sorted, result];
}
// Try logging your results to test your code!
console.log(alphabetizer(moonWalkers));