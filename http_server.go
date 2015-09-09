package main

import (
	// "fmt"
	"io"
	"net/http"
	"strconv"
	// "time"

	// "github.com/golang/glog"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// start := time.Now()
	// fmt.Fprintf(w, "Hello World")
	// fmt.Println(time.Since(start))

	result := "Hello, world.\n"
	w.Header().Set("Content-type", "type/plain")
	w.Header().Set("Content-Length", strconv.Itoa(len(result)))
	io.WriteString(w, result)
}
