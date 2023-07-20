

dev-build:
	docker-compose -f docker-compose.dev.yaml build

prod-build:
	docker-compose -f docker-compose.prod.yaml build

dev-up:
	docker-compose -f docker-compose.dev.yaml up -d

prod-up:
	docker-compose -f docker-compose.prod.yaml up -d

dev-down:
	docker-compose -f docker-compose.dev.yaml down

prod-down:
	docker-compose -f docker-compose.prod.yaml down
