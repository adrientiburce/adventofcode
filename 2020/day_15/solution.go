package main

import (
	"fmt"
	"time"
)

func main() {
	start := time.Now()
	part2()
	fmt.Printf("It took %s \n", time.Since(start))
}

func part2() {
	spokenNumbers := map[int]int{20: 1, 9: 2, 11: 3, 0: 4, 1: 5, 2: 0}
	var nextSpoken, beforeLastSpoken int
	lastSpoken := 2
	turn := len(spokenNumbers) + 1
	for turn <= 30000000 {
		beforeLastSpoken = spokenNumbers[lastSpoken]
		if beforeLastSpoken == 0 {
			nextSpoken = 0
		} else {
			nextSpoken = turn - 1 - beforeLastSpoken
		}
		// update last turn
		spokenNumbers[lastSpoken] = turn - 1
		lastSpoken = nextSpoken
		turn++
	}
	fmt.Println(lastSpoken)
}

func naivePart1() {
	spokenNumbers := []int{20, 9, 11, 0, 1, 2}
	i := len(spokenNumbers) + 1
	lastSpoken := spokenNumbers[i-2]
	nextSpoken := 0
	for i <= 2020 {
		n := i - 1
		findBeforeLast := indexReverse(lastSpoken, spokenNumbers[:n-1])
		if findBeforeLast == -1 {
			nextSpoken = 0
		} else {
			nextSpoken = n - findBeforeLast - 1
		}
		spokenNumbers = append(spokenNumbers, nextSpoken)
		lastSpoken = nextSpoken
		i += 1
	}
	fmt.Println(spokenNumbers[len(spokenNumbers)-1])
}

func indexReverse(el int, data []int) int {
	for i := len(data) - 1; i >= 0; i-- {
		if el == data[i] {
			return i
		}
	}
	return -1 //not found.
}
