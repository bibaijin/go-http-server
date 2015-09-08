package main

import (
	"fmt"
	"net/http"

	// "github.com/golang/glog"
)

func handler(w http.ResponseWriter, r *http.Request) {
	// fmt.Fprintf(w, "Hi there, I love %s.\n", r.URL.Path[1:])
	fmt.Fprintf(w, "Hello, world")
	// glog.Info("here")
}
