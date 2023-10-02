/////////////////////////////////////////////////////////////////////////////////
// Rewards properties:
// - rewards count can only increase
// - rewards count can only be increased by Emmision manager
// - rewards count can only be increased via configureAssets function
// - getAvailableRewardsCount(asset)  i.e. _assets[asset].availableRewardsCount
//   and getRewardsByAsset(asset).length should be equal
/////////////////////////////////////////////////////////////////////////////////
rule availableRewardsCountProperties(method f, env e, calldataarg args, address asset, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    uint256 _availableRewardsCount = getAvailableRewardsCount(asset);
    address[] _rewards = getRewardsByAsset(e, asset);

    require _rewards.length == _availableRewardsCount;

    f@withrevert(e, args);

    uint256 availableRewardsCount_ = getAvailableRewardsCount(asset);
    address[] rewards_ = getRewardsByAsset(e, asset);

    assert availableRewardsCount_ >= _availableRewardsCount;
    assert availableRewardsCount_ >  _availableRewardsCount
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector );
    assert availableRewardsCount_ == rewards_.length;
}

/////////////////////////////////////////////////////////////////////////////////
// claimRewards properties
// - claimRewards to address zero should revert
// - claimRewards with no asset should give zero reward
// - claimRewards with amount zero should give zero reward
// - claimRewards on reward equal to address 0 should give zero reward
// - claimRewards with asset equal to address 0 should give zero reward
/////////////////////////////////////////////////////////////////////////////////
rule claimRewardsReverts(env e, address[] assets, uint256 amount, address to, address reward){
  uint256 claimed = 0;

  claimed = claimRewards@withrevert(e, assets, amount, to, reward);

  assert ( to == 0 )            => lastReverted;

  assert ( assets.length == 0 ) => claimed == 0;
  assert ( amount == 0 )        => claimed == 0;
  assert ( reward == 0 )        => claimed == 0;
  assert ( ( assets.length == 1 ) && ( assets[0] == 0 )  ) => claimed == 0;
}

/////////////////////////////////////////////////////////////////////////////////
// claimRewardsOnBehalfReverts properties
// - claimRewards to address zero should revert
// - claimRewards from user equal to address zero should revert
/////////////////////////////////////////////////////////////////////////////////
rule claimRewardsOnBehalfReverts(env e, address[] assets, uint256 amount, address user, address to, address reward){
  claimRewardsOnBehalf@withrevert(e, assets, amount, user, to, reward);

  assert ( to == 0   )          => lastReverted;
  assert ( user == 0 )          => lastReverted;
}

/////////////////////////////////////////////////////////////////////////////////
// claimAllRewards properties
// - claimRewards to address zero should revert
/////////////////////////////////////////////////////////////////////////////////
rule claimAllRewardsReverts(env e, address[] assets, address to){
  claimAllRewards@withrevert(e, assets, to);

  assert ( to == 0 )            => lastReverted;
}

/////////////////////////////////////////////////////////////////////////////////
// claimAllRewardsOnBehalfReverts properties
// - claimRewards to address zero should revert
// - claimRewards from user equal to address zero should revert
/////////////////////////////////////////////////////////////////////////////////
rule claimAllRewardsOnBehalfReverts(env e, address[] assets, address user, address to){
  claimAllRewardsOnBehalf@withrevert(e, assets, user, to);

  assert ( to == 0 )            => lastReverted;
  assert ( user == 0 )          => lastReverted;
}
