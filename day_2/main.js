const fs = require('fs');

//#############################
// CONSTANTS
//#############################

const data = fs.readFileSync('input', 'utf8');
const values = {"X": 1, "Y":2, "Z":3, "A":1, "B": 2, "C":3}
const winCases = ["23", "12", "31"]


//#############################
// FUNCTIONS
//#############################

const calculateScore = (listOfMatches, part_two=false) => {
    const matches = listOfMatches.split("\r\n")
    let score = 0
    matches.forEach(match => {
        [opponentChoice, elfChoice]  = match.split(" ")
        let matchToInt=values[opponentChoice].toString() + values[elfChoice].toString()
        if (part_two && matchToInt[1] == "3") {winCases.forEach(x => {if(x[0]==matchToInt[0]){matchToInt=x}})}
        else if (part_two && matchToInt[1] == "2") {matchToInt = (matchToInt[0] + matchToInt[0])}
        else if (part_two && matchToInt[1] == "1") {winCases.forEach(x => {if(x[1]==matchToInt[0]){matchToInt=(x[1]+x[0])}})} 
        if(winCases.includes(matchToInt)){score+=6}
        else if(matchToInt[0]==matchToInt[1]){score+=3}
        score+=parseInt(matchToInt[1])
    });

    return score
}

//#############################
// ENTRY
//#############################
console.log(calculateScore(data))
console.log(calculateScore(data, part_two=true))