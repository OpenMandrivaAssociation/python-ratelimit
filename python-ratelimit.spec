%define module ratelimit

Name:		python-%{module}
Version:	2.2.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/r/%{module}/%{module}-%{version}.tar.gz
Summary:	API rate limit decorator
URL:		https://pypi.org/project/ratelimit/
License:	MIT
Group:		Development/Python

BuildRequires:	python%{pyver}dist(setuptools)
BuildSystem:	python
BuildArch:	noarch

%description
APIs are a very common way to interact with web services. 
As the need to consume data grows, so does the number of API calls necessary 
to remain up to date with data sources. 
However many API providers constrain developers from making too many API calls. 
This is know as rate limiting and in a worst case scenario your application can be banned from 
making further API calls if it abuses these limits.

This packages introduces a function decorator preventing a function from being called 
more often than that allowed by the API provider. 
This should prevent API providers from banning your applications by 
conforming to their rate limits.

%files
%{python_sitelib}/%{module}/
%{python_sitelib}/%{module}-%{version}-py%{python_version}.egg-info
