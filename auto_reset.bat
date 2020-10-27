@Echo OFF

cd ..

echo "%~dp0"

pause

For /F %%G in ('DIR /S /B /A:D .git') Do (
	cd %%G
	cd ../
	Echo updating %%G
	git reset
)


popd
pause