

20210881 하승훈

"배달의 민족" 앱의 사용 흐름을 기반으로 음식 주문 과정을 소프트웨어적으로 모델링하고,  
시퀀스 다이어그램 → 샘플 코드 구현 → 모듈 평가까지 순서대로 수행하였습니다.

---
사용 사례

사용자는 배가 고플 때 앱을 실행해 음식점을 검색하고,
메뉴를 고른 뒤 결제 및 주문을 완료합니다.

---
스퀸스 다이어그램

https://mermaid.live/edit#pako:eNqFk12L00AUhv9KmOu2NGm2SeaisCp4K4o3kpuhGbvBzYfTRK2lIGwRSyta2Iq7NJCyIqwoxHWFvVj_kDP5D07z0TZtbXM1mfO855x35kwXNB0DAwja-LmP7Sa-Z6IWQZZuC_xzEfHMpuki2xMetzHZ3L2DsGXah667GXqEyYttkoe47SGf8OVm7AHqWNj27iMPv0Qd3U6Jeelyo7GoBQU2-Smw4Zf400Cg0QeBBSM2DFj4Ufh79YadDFLZgufatBm4QtJvl3QWCOz8lF39SAUpVF4rtaEIxnT4e70EF83b3MLH4ykbTnd4WQhYP4xPgsQRvTylg2uBzaL4fLTDTqKIJ9PVspl0n7GMo-8jFlzH_WifsYzfZycvv_TCLm7p95tCQ6teincO-RVGLJwW8CKy5iPnz_r0YpT3tfWwsj7CCf3FGwz77O2scD6NxnI2V_AltwyXt-R995kGf3ZNUp5wzFEhPpuw4Ob_Y5TBiSs-7yP69RaUQIuYBoAe8XEJWJhYaP4LuvM0OvCOsIV1APnSQOSZDnS7xzX8ZT1xHCuXEcdvHQH4FB23-Z_vGvxUs1e_QLBtYHLX8W0PQC3JAGAXvAJQlOVKVZFqYlWry5qi1ni0A6Akq5WaUldFTZJkTVLrB70SeJ0UrVbqVb4lqopSU2VRPVB7_wDEBeHX

---

샘플 코드

`app.py` 파일에 Python으로 구현된 시나리오 코드가 포함되어 있습니다.

---

모듈 평가

|   항목    |  평가 내용 |
|----------|-----------|
|   응집도  | 각 클래스는 명확하게 분리된 책임을 가지고 있으며, 단일 책임 원칙(SRP)을 잘 따르고 있습니다. |
|   결합도  | 클래스 간 상호작용은 메서드를 통해 수행되며, 내부 구현에는 의존하지 않으므로 결합도가 낮고 유지보수가 용이합니다. |