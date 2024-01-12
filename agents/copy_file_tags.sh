#!/bin/bash
copy_paste_file_tags() {
    source="$1"
    for target in "${@:2}"; do
        tags="$(file_tags $source)"
        old_tags="$(file_tags "$target")"
        tags="$tags,$old_tags"
        set_file_tags "$target" "$tags"
        getfattr --name=user.xdg.tags --only-values "$target"
    done
}

copy_paste_file_rating() {
    source="$1"
    for target in "${@:2}"; do
        rating=$(file_rating "$source")
        set_file_rating "$target" "$rating"
        rating: "$(file_rating $target)"
    done
    }

star_rating() {
    getfattr --name=user.baloo.rating --only-values "$1"
    }

file_tags() {
    getfattr --name=user.xdg.tags --only-values "$1"
    }

set_star_rating() {
    target="$1"
    rating="$2"
    setfattr --name=user.baloo.rating --value="$rating" "$target"
    }

set_file_tags() {
    target="$1"
    tags="$2"
    setfattr --name=user.xdg.tags --value="$tags" "$target"
    }

copy_tags_and_stars() {
    copy_paste_file_tags "$@"
    copy_paste_file_rating "$@"
    }