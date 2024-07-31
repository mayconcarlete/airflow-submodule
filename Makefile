.PHONY: makefolders

USER:=$(id -u)

USER_GROUP:="$(id -g)"

makefolders:
	@mkdir -p data
	@mkdir -p data/postgresql/data

makeUser:
	echo "value: ${USER_GROUP} - ${USER}"