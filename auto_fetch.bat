@Echo OFF

cd ..

For /F %%G in ('DIR /S /B /A:D .git') Do (
	cd %%G
	cd ../
	Echo Fetch %%G
	git fetch
)


popd
pause