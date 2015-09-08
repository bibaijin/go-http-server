package main

import (
	"flag"
	"net/http"
)

func main() {
	flag.Parse()

	http.HandleFunc("/", handler)
	http.ListenAndServe(":8081", nil)
}
