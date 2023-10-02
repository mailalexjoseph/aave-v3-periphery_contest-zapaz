using DummyERC20_rewardToken as Reward;

methods {
  // More RewardsController
  function getAssetDecimals(address)                      external returns (uint8)                               envfree;
  function getRewardsByAsset(address)                     external returns (address[])                           envfree;
  function getRewardsList()                               external returns (address[])                           envfree;
  function getTransferStrategy(address)                   external returns (address)                             envfree;
  function getRewardOracle(address)                       external returns (address)                             envfree;
  function REVISION()                                     external returns (uint256)                             envfree;
  function EMISSION_MANAGER()                             external returns (address)                             envfree;

  function getAssetIndex(address,address)                 external returns (uint256,uint256);

  // More RewardsControllerHarnes
  function getAssetsList()                                external returns (address[])                           envfree;
  function getAvailableRewardsCount(address)              external returns (uint128)                             envfree;
  function inArray(address[],address)                     external returns (bool)                                envfree;
  function isContract(address)                            external returns  (bool)                               envfree;
  function isRewardEnabled(address)                       external returns  (bool)                               envfree;
  function rewardOracle()                                 external returns (address)                             envfree;
  function getLastUpdateTimestamp(address,address)        external returns (uint256)                             envfree;
  function getUserAccruedReward(uint256,address,address)  external returns (uint256)                             envfree;
  // function getRewardsListLength()                         external returns (uint256)                             envfree;
  // function getRewardsByAssetLength(address)               external returns (uint256)                             envfree;

  // function getRewardsDataHarness(address, address)        external returns (uint104, uint88, uint32, uint32);
  // function getAssetIndexNew(address,address)              external returns (uint104);
  function configureAsset(address,address,address)        external;

  // More AToken
  function _.mint(address,uint128)                       external                                               envfree;
}
