@Echo OFF

cd ..

For /F %%G in ('DIR /S /B /A:D .git') Do (
	cd %%G
	cd ../
	Echo ----------------------------------------------------
	Echo Checking %%G
	git status
)


popd
pause