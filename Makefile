all: clean build install

build:
	sh build.sh

clean:
	rm -rf 'dist/Equalize Sidebearings.roboFontExt'

install:
	open 'dist/Equalize Sidebearings.roboFontExt'

archive: clean build
	rm -f dist/Equalize-Sidebearings.roboFontExt.zip
	cd dist && zip -r Equalize-Sidebearings.roboFontExt.zip 'Equalize Sidebearings.roboFontExt'
