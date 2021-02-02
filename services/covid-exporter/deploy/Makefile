# Makefile for covid-exporter service

IMAGE_NAME := covid-exporter
REPO_ROOT := $(shell git rev-parse --show-toplevel)
BUILD_DIR := $(REPO_ROOT)/services/$(IMAGE_NAME)
TAG ?= latest
MAKEFLAGS += --no-print-directory

# built-in targets
.PHONY: help build build-nc clean tag
.DEFAULT_GOAL := help

# targets
help: ## this help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: ## build the image
	@cd $(REPO_ROOT); \
	docker build -t $(IMAGE_NAME):$(TAG) -f$(BUILD_DIR)/deploy/Dockerfile $(ARGS) .
	@EXIT_CODE=$?
	@exit $(EXIT_CODE)

build-nc: ## build the image using --no-cache
	@make build ARGS="--no-cache"

build-dev: ## build the image up to development with tag:development
	@make build

clean: ## clean the image
	docker image rm $(IMAGE_PREFIX)-$(IMAGE_NAME):$(TAG)

