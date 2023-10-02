/////////////////////////////////////////////////////////////////////////////////
// Ensure asset is immutable
// - any (non zero) asset in assetsList cannot be changed
// - assetList length can only increase
/////////////////////////////////////////////////////////////////////////////////
rule setupAssetImmutable(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    address[] _assetsList = getAssetsList();
    uint256 _assetsListLength = _assetsList.length;
    uint256 index;
    require _assetsListLength <= 2;
    require index < _assetsListLength;

    address _asset = _assetsList[index];

    f@withrevert(e, args);

    address[] assetsList_ = getAssetsList();
    uint256 assetsListLength_ = assetsList_.length;
    address asset_ = assetsList_[index];

    assert asset_ == _asset;
    assert assetsListLength_ >= _assetsListLength;
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure asset can only be added by Emmission manager via configureAssets function
/////////////////////////////////////////////////////////////////////////////////
rule setupAssetsAdded(method f, env e, calldataarg args) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    address[] _assetsList = getAssetsList();
    mathint _assetsListLength = _assetsList.length;
    require _assetsListLength <= 2;
    
    f@withrevert(e, args);

    address[] assetsList_ = getAssetsList();
    mathint assetsListLength_ = assetsList_.length;

    assert assetsListLength_ > _assetsListLength
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector );
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure properties on asset config modifications
// - emissionPerSecond can only be modified by Emission manager via
//   configureAssets or setEmissionPerSecond functions
// - distributionEnd_ can only be modified by Emission manager via
//   configureAssets or setDistributionEnd functions
/////////////////////////////////////////////////////////////////////////////////
rule setupRewardModified(method f, env e, calldataarg args, address asset, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
} {
    uint256 _index; uint256 _emissionPerSecond; uint256 _lastUpdateTimestamp; uint256 _distributionEnd;
    _index, _emissionPerSecond, _lastUpdateTimestamp, _distributionEnd =  getRewardsData(e, asset, reward);

    f@withrevert(e, args);

    uint256 index_; uint256 emissionPerSecond_; uint256 lastUpdateTimestamp_; uint256 distributionEnd_;
    index_, emissionPerSecond_, lastUpdateTimestamp_, distributionEnd_ =  getRewardsData(e, asset, reward);

    assert emissionPerSecond_ != _emissionPerSecond
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||   (  ( f.selector == sig:setEmissionPerSecond(address,address[],uint88[]).selector )
           && ( _lastUpdateTimestamp != 0 ) );

    assert distributionEnd_ != _distributionEnd
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setDistributionEnd(address,address,uint32).selector             ) );
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure transferStrategy can only be modified by Emmission manager
//  via configureAssets or setTransferStrategy functions
//  and that transferStrategy is not zero
/////////////////////////////////////////////////////////////////////////////////
rule setupTransferStrategy(method f, env e, calldataarg args, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _transferStrategy = getTransferStrategy(reward);
    f@withrevert(e, args);
    address transferStrategy_ = getTransferStrategy(reward);

    assert transferStrategy_ != _transferStrategy
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   transferStrategy_ != 0
      &&   isContract(transferStrategy_)
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setTransferStrategy(address,address).selector                   ) );
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure rewardOracle can only be modified by Emmission manager
//  via configureAssets or setRewardOracle functions
/////////////////////////////////////////////////////////////////////////////////
rule setupRewardOracle(method f, env e, calldataarg args, address reward) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _rewardOracle = getRewardOracle(reward);
    f@withrevert(e, args);
    address rewardOracle_ = getRewardOracle(reward);

    assert rewardOracle_ != _rewardOracle
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( ( f.selector == sig:configureAssets(RewardsDataTypes.RewardsConfigInput[]).selector )
      ||     ( f.selector == sig:setRewardOracle(address,address).selector                       ) );
}

/////////////////////////////////////////////////////////////////////////////////
// Ensure claimer can only be modified by Emmission manager via setClaimer function
/////////////////////////////////////////////////////////////////////////////////
rule setupClaimer(method f, env e, calldataarg args, address user) filtered {
   f -> !f.isView && !harnessFunction(f)
}{
    address _claimer = getClaimer(user);
    f@withrevert(e, args);
    address claimer_ = getClaimer(user);

    assert claimer_ != _claimer
      =>   ( e.msg.sender == EMISSION_MANAGER() )
      &&   ( f.selector == sig:setClaimer(address,address).selector );
}

