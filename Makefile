build:
	docker compose build

up:
	docker compose up

down:
	docker compose down

clean:
	docker compose down -v

intake:
	python tools/intake_extractor.py
	python tools/intake_router.py
	python tools/intake_integrator.py