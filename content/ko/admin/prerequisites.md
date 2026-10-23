---
title: 컴퓨터 준비하기
menu:
  docs:
    weight: 10
    parent: admin
---

새 컴퓨터를 설정한다면 먼저 보안을 강화하는 것을 권장합니다. **Ubuntu 22.04**를 사용한다고 가정합니다.

## 비밀번호 기반 SSH 로그인을 허용하지 않기(키만 허용) {#do-not-allow-password-based-ssh-login-keys-only}

먼저 실제로 비밀번호가 아닌 키로 서버에 로그인하고 있는지 확인합니다. 그렇지 않으면 서버에 접근할 수 없게 됩니다. 많은 호스팅 제공자가 공개 키 업로드를 지원하고 새 컴퓨터에 키 기반 root 로그인을 자동 설정합니다.

`/etc/ssh/sshd_config`를 편집하고 `PasswordAuthentication`을 찾습니다. 주석이 해제되어 있고 `no`로 설정되어 있어야 합니다. 변경했다면 sshd를 재시작합니다.

```bash
systemctl restart ssh.service
```

## 시스템 패키지 업데이트 {#update-system-packages}

```bash
apt update && apt upgrade -y
```

## 반복 로그인 시도를 차단하도록 fail2ban 설치 {#install-fail2ban-so-it-blocks-repeated-login-attempts}

먼저 fail2ban을 설치합니다.

```bash
apt install fail2ban
```

`/etc/fail2ban/jail.local`을 편집하고 다음 내용을 넣습니다.

```text
[DEFAULT]
destemail = your@email.here
sendername = Fail2Ban

[sshd]
enabled = true
port = 22
mode = aggressive
```

마지막으로 fail2ban을 재시작합니다.

```bash
systemctl restart fail2ban
```

서비스가 "Failed during configuration: Have not found any log file for sshd jail" 오류로 실패한다면,
`[sshd]` 절에 `backend=systemd` 줄을 추가하여 로그 기록을 systemd로 전환합니다.
`python3-systemd` 패키지를 설치해야 할 수도 있습니다.


## 방화벽을 설치하고 SSH, HTTP, HTTPS 포트만 허용하기 {#install-a-firewall-and-only-allow-ssh-http-and-https-ports}

먼저 iptables-persistent를 설치합니다. 설치 중 현재 규칙을 유지할지 물으면 거절합니다.

```bash
apt install -y iptables-persistent
```

`/etc/iptables/rules.v4`를 편집하고 다음 내용을 넣습니다.

```text
*filter

#  Allow all loopback (lo0) traffic and drop all traffic to 127/8 that doesn't use lo0
-A INPUT -i lo -j ACCEPT
-A INPUT ! -i lo -d 127.0.0.0/8 -j REJECT

#  Accept all established inbound connections
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

#  Allow all outbound traffic - you can modify this to only allow certain traffic
-A OUTPUT -j ACCEPT

#  Allow HTTP and HTTPS connections from anywhere (the normal ports for websites and SSL).
-A INPUT -p tcp --dport 80 -j ACCEPT
-A INPUT -p tcp --dport 443 -j ACCEPT
#  (optional) Allow HTTP/3 connections from anywhere.
-A INPUT -p udp --dport 443 -j ACCEPT

#  Allow SSH connections
#  The -dport number should be the same port number you set in sshd_config
-A INPUT -p tcp -m state --state NEW --dport 22 -j ACCEPT

#  Allow ping
-A INPUT -p icmp -m icmp --icmp-type 8 -j ACCEPT

# Allow destination unreachable messages, especially code 4 (fragmentation required) is required or PMTUD breaks
-A INPUT -p icmp -m icmp --icmp-type 3 -j ACCEPT

#  Log iptables denied calls
-A INPUT -m limit --limit 5/min -j LOG --log-prefix "iptables denied: " --log-level 7

#  Reject all other inbound - default deny unless explicitly allowed policy
-A INPUT -j REJECT
-A FORWARD -j REJECT

COMMIT
```

iptables-persistent를 사용하면 부팅할 때 해당 설정을 불러옵니다. 지금은 재부팅하지 않으므로 처음 한 번은 수동으로 불러와야 합니다.

```bash
iptables-restore < /etc/iptables/rules.v4
```

서버에 IPv6로도 접근할 수 있다면 `/etc/iptables/rules.v6`를 편집하고 다음 내용을 추가합니다.
```text
*filter

#  Allow all loopback (lo0) traffic and drop all traffic to 127/8 that doesn't use lo0
-A INPUT -i lo -j ACCEPT
-A INPUT ! -i lo -d ::1/128 -j REJECT

#  Accept all established inbound connections
-A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

#  Allow all outbound traffic - you can modify this to only allow certain traffic
-A OUTPUT -j ACCEPT

#  Allow HTTP and HTTPS connections from anywhere (the normal ports for websites and SSL).
-A INPUT -p tcp --dport 80 -j ACCEPT
-A INPUT -p tcp --dport 443 -j ACCEPT
#  (optional) Allow HTTP/3 connections from anywhere.
-A INPUT -p udp --dport 443 -j ACCEPT

#  Allow SSH connections
#  The -dport number should be the same port number you set in sshd_config
-A INPUT -p tcp -m state --state NEW --dport 22 -j ACCEPT

#  Allow ping
-A INPUT -p icmpv6 -j ACCEPT

#  Log iptables denied calls
-A INPUT -m limit --limit 5/min -j LOG --log-prefix "iptables denied: " --log-level 7

#  Reject all other inbound - default deny unless explicitly allowed policy
-A INPUT -j REJECT
-A FORWARD -j REJECT

COMMIT
```
IPv4 규칙과 비슷하게 다음과 같이 수동으로 불러올 수 있습니다.
```bash
ip6tables-restore < /etc/iptables/rules.v6
```
