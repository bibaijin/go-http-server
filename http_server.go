package main

import (
	"io"
	"net/http"
	"strconv"

	// "github.com/golang/glog"
)

func handler(w http.ResponseWriter, r *http.Request) {
	result := "Hello, world.\n"
	w.Header().Set("Content-type", "type/plain")
	w.Header().Set("Content-Length", strconv.Itoa(len(result)))
	io.WriteString(w, result)
}
