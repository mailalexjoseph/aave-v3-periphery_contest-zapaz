// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.10;

import {RewardsController} from "../../contracts/rewards/RewardsController.sol";
import {RewardsDataTypes} from "../../contracts/rewards/libraries/RewardsDataTypes.sol";
import {ITransferStrategyBase} from "../../contracts/rewards/interfaces/ITransferStrategyBase.sol";
import {IEACAggregatorProxy} from "../../contracts/misc/interfaces/IEACAggregatorProxy.sol";

contract RewardOracleHarness {
    function latestAnswer() external returns (uint256) {
        return 42;
    }
}

contract RewardsControllerHarness is RewardsController {
    address public rewardOracle;

    constructor(address emissionManager) RewardsController(emissionManager) {
        rewardOracle = address(new RewardOracleHarness());
    }

    function userRewardCalculate(
        uint32 currentTimestamp,
        uint32 lastUpdateTimestamp,
        uint88 emissionPerSecond,
        uint104 assetIndex,
        uint104 userIndex,
        uint128 userAccrued,
        uint256 userBalance,
        uint256 totalSupply,
        uint256 assetUnit
    ) external pure returns (uint256) {
        uint256 userPendingIndex = uint256(assetIndex - userIndex);
        uint256 userPending = uint256(userBalance * userPendingIndex / assetUnit);

        uint256 deltaTime = uint256(currentTimestamp - lastUpdateTimestamp);
        uint256 deltaEmission = uint256(emissionPerSecond * deltaTime * assetUnit);
        uint256 deltaIndex = uint256(deltaEmission / totalSupply);

        uint256 claimable = uint256(userPending + userAccrued);

        return claimable;
    }

    function getAssetRewardIndex(address asset, address reward) external view returns (uint256) {
        return _assets[asset].rewards[reward].index;
    }

    // function getRewardsByAssetLength(address asset) public view returns (uint256) {
    //     return this.getRewardsByAsset(asset).length;
    // }

    // function getRewardsListLength() public view returns (uint256) {
    //     return this.getRewardsList().length;
    // }
    //
    // function getAssetIndexNew(address asset, address reward) public view returns (uint104 index) {
    //     (, uint256 newIndex) = this.getAssetIndex(asset, reward);
    //     index = uint104(index);
    // }
    //
    // function getRewardsDataHarness(address asset, address reward)
    //     public
    //     view
    //     returns (uint104 index, uint88 emissionPerSecond, uint32 lastUpdateTimestamp, uint32 distributionEnd)
    // {
    //     index = getAssetIndexNew(asset, reward);
    //     emissionPerSecond = _assets[asset].rewards[reward].emissionPerSecond;
    //     lastUpdateTimestamp = _assets[asset].rewards[reward].lastUpdateTimestamp;
    //     distributionEnd = _assets[asset].rewards[reward].distributionEnd;
    // }
    //
    // function getEmissionPerSecond(address asset, address reward) external view returns (uint256) {
    //     return _assets[asset].rewards[reward].emissionPerSecond;
    // }

    function isRewardEnabled(address reward) external view returns (bool) {
        return _isRewardEnabled[reward];
    }

    function getAssetsList() external view returns (address[] memory) {
        return _assetsList;
    }

    function getLastUpdateTimestamp(address asset, address reward) external view returns (uint256) {
        return _assets[asset].rewards[reward].lastUpdateTimestamp;
    }

    function getAvailableRewardsCount(address asset) external view returns (uint128) {
        return _assets[asset].availableRewardsCount;
    }

    function _createConfigAsset(address asset, address reward, address transferStrategy)
        internal
        returns (RewardsDataTypes.RewardsConfigInput memory config)
    {
        config.asset = asset;
        config.reward = reward;
        config.transferStrategy = ITransferStrategyBase(transferStrategy);
        config.rewardOracle = IEACAggregatorProxy(rewardOracle);
    }

    function configureAsset(address asset, address reward, address transferStrategy) external {
        RewardsDataTypes.RewardsConfigInput[] memory configs = new RewardsDataTypes.RewardsConfigInput[](1);
        configs[0] = _createConfigAsset(asset, reward, transferStrategy);

        this.configureAssets(configs);
    }

    function getUserAccruedReward(uint256 i, address user, address reward) public view returns (uint256) {
        return _assets[_assetsList[i]].rewards[reward].usersData[user].accrued;
    }

    function isContract(address account) external view returns (bool) {
        return _isContract(account);
    }

    function inArray(address[] memory array, address addr) public pure returns (bool) {
        for (uint256 i = 0; i < array.length; i++) {
            if (array[i] == addr) {
                return true;
            }
        }
        return false;
    }
}
