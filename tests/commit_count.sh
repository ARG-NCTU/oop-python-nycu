for i in {1..15}; do
	echo "Group $i "
	git shortlog -sn --since="2025-09-01" -- "group$i/" | grep -Ev '^[[:space:]]*[0-9]+[[:space:]]+(Brian2074|Brian Lan)$'
done
