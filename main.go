package main

import (
	"flag"
	// "fmt"
	"net/http"
	"runtime"
	"strconv"
)

func main() {
	var port, amount int
	flag.IntVar(&port, "port", 8081, "listen port")
	flag.IntVar(&amount, "amount", 1, "amount")
	flag.Parse()

	// fmt.Println(runtime.NumCPU())
	runtime.GOMAXPROCS(4)

	done := make(chan bool)
	http.HandleFunc("/", handler)
	for i := 0; i < amount; i++ {
		go http.ListenAndServe(":"+strconv.Itoa(8081+i), nil)
	}
	<-done
}
