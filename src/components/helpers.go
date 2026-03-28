package helpers

import (
	"encoding/json"
	"errors"
	"fmt"
	"log"
	"net/http"
	"strings"

	"github.com/frontend-app/models"
)

func parseJSONBody(r *http.Request, target interface{}) error {
	if r.Header.Get("Content-Type")!= "application/json" {
		return errors.New("invalid content type, expected application/json")
	}

	err := json.NewDecoder(r.Body).Decode(target)
	if err!= nil {
		return fmt.Errorf("failed to decode JSON: %w", err)
	}

	return nil
}

func parseQueryString(r *http.Request, key string) (string, error) {
	value, ok := r.URL.Query()[key]
	if!ok {
		return "", fmt.Errorf("query parameter '%s' not found", key)
	}

	return value[0], nil
}

func handleAPIError(w http.ResponseWriter, err error, status int) {
	log.Printf("API error: %v\n", err)
	http.Error(w, "Internal Server Error", status)
}

func validateUserInput(input string) (string, error) {
	input = strings.TrimSpace(input)
	if input == "" {
		return "", errors.New("input cannot be empty")
	}

	return input, nil
}

func getUserFromContext(r *http.Request) (*models.User, error) {
	user, ok := r.Context().Value("user").(*models.User)
	if!ok {
		return nil, errors.New("user not found in context")
	}

	return user, nil
}