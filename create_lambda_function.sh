aws lambda create-function \
--function-name my-math-function \
--zip-file fileb://my-deployment-package.zip \
--handler lambda_function.lambda_handler \
--runtime python3.8 \
--role arn:aws:iam::644100745902:role/service-role/pull-coingecko-price-data-role-oj11ry5y