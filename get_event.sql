SELECT
  *
FROM ethereum.logs
WHERE
  "contract_address" = 0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9
AND topic0 = from_hex('bc7cd75a20ee27fd9adebab32041f755214dbc6bffa90cc0225b39da2e5c2d3b')
