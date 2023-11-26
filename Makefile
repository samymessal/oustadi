all: 
	docker compose -f ./srcs/docker-compose.yml build
	docker compose -f ./srcs/docker-compose.yml up -d

start:
	docker compose -f ./srcs/docker-compose.yml up -d

stop:
	docker container stop gpt-assistant

logs:
	docker logs gpt-assistant

clean:
	docker container stop gpt-assistant

fclean: clean
	@docker system prune -af

re: fclean all

.Phony: all logs clean fclean