---
title: 역할
description: 관리자 대시보드에서 역할을 관리합니다.
menu:
  docs:
    parent: admin
---

# 역할 {#roles}
데이터베이스에 초기 데이터를 넣을 때 [`~/config/roles.yml`](https://github.com/mastodon/mastodon/blob/main/config/roles.yml)의 값을 바탕으로 역할을 만듭니다.

{{< page-ref page="entities/Role" >}}

그 결과 생성되는 [기본 역할](#default-roles)은 `Owner`, `Admin`, `Moderator`입니다.

*역할*(`/admin/roles`) 페이지의 [역할 추가](#add-role)로 역할과 속성을 만들 수 있습니다.

![역할 관리 화면](/assets/admin-roles-ui.png)

기존 역할의 속성은 [역할 편집](#edit-role) 기능으로 변경할 수 있습니다.

## 기본 역할 {#default-roles}
### 기본 역할(*기본 권한*) {#default-base-role}

역할이 지정되지 않은 사용자를 포함한 모든 사용자에게 영향을 줍니다.

이 역할에서 변경할 수 있는 유일한 권한 플래그는 **사용자 초대**입니다. 이 권한을 활성화하면 모든 사용자가 초대를 보낼 수 있습니다.

기본 역할의 우선순위는 `0`이며 변경할 수 없습니다.

### 소유자 {#default-owner-role}

모든 권한을 우회하는 **관리자** 권한 플래그가 부여된 역할입니다. 소유자 역할의 사용자는 모든 [권한 플래그](/entities/Role/#permission-flags)가 활성화됩니다.

역할의 *이름*, *배지 색상*, *배지 표시* 속성을 바꿀 수 있습니다. 이 역할의 권한은 편집하거나 취소할 수 없습니다.

소유자 역할은 모든 역할 중 가장 높은 [우선순위](#role-priority)(`1000`)를 갖습니다. 소유자는 다른 모든 역할의 속성을 수정할 수 있습니다. 새 역할과 기존 역할의 [우선순위](#role-priority)는 `999` 이하여야 하므로 소유자 역할보다 높은 역할을 만들 수 없습니다.

### 관리자 {#default-admin-role}

모든 **중재** 및 **관리** 권한 플래그가 부여된 역할입니다.

이 역할의 **DevOps** 권한 플래그는 비활성화되어 있지만 **소유자** 또는 더 높은 우선순위의 사용자 정의 역할이 활성화할 수 있습니다.

역할의 *이름*, *배지 색상*, *배지 표시* 속성을 바꿀 수 있습니다.

관리자 역할의 우선순위는 `100`입니다.

### 중재자 {#default-moderator-role}

일부 **중재** 권한 플래그가 부여된 역할입니다. 다음 권한이 포함됩니다.
- **대시보드 보기**
- **감사 로그 보기**
- **사용자 관리**
- **신고 관리**
- **분류 관리**

역할의 *이름*, *배지 색상*, *배지 표시* 속성을 바꿀 수 있습니다.

중재자 역할의 우선순위는 `10`입니다.

## 역할 추가 {#add-role}

`admin/roles/new` 페이지에서 사용자 정의 역할을 만들 수 있습니다.

![새 역할 추가 화면](/assets/admin-roles-new-ui.png)

### 입력 필드 {#add-role-input-fields}

{{< page-relref ref="entities/Role#name" caption="이름">}}

역할 이름은 중복될 수 있습니다. 데이터베이스에서는 `id`로 구분하며, 웹 인터페이스에서는 ID를 설정할 수 없습니다.

{{< page-relref ref="entities/Role#color" caption="배지 색상">}}

### 우선순위 {#role-priority}

- 기본값은 `0`입니다.
	- `999`보다 클 수 없습니다.
	- 음의 정수도 사용할 수 있습니다.
- 두 역할이 같은 우선순위 값을 가질 수 있습니다.

> “특정 상황에서는 더 높은 역할이 충돌 해결을 결정합니다. 일부 작업은 우선순위가 더 낮은 역할에 대해서만 수행할 수 있습니다.”

{{< page-relref ref="entities/Role#highlighted" caption="사용자 프로필에 역할을 배지로 표시">}}

{{< page-relref ref="entities/Role#permissions" caption="권한">}}


## 역할 편집 {#edit-role}

![역할 편집 메뉴](/assets/admin-roles-edit-ui.png)

역할 목록의 *편집*으로 기존 역할과 속성을 편집할 수 있습니다. 새 역할을 만들 때처럼 [입력 필드](#add-role-input-fields)를 변경하고 저장할 수 있습니다. 이 양식에서 역할을 삭제할 수도 있습니다.

![역할 속성 편집 화면](/assets/admin-roles-edit-role-ui.png)

**역할 관리** 권한으로 로그인한 사용자는 항상 모든 역할을 볼 수 있지만, 자신에게 지정된 역할보다 [우선순위](#role-priority)가 높거나 같은 역할은 수정할 수 없습니다.
