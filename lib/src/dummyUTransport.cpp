#include <up-client-dummy-cpp/transport/dummyUTransport.h>

#include <spdlog/spdlog.h>

UStatus DummyUTransport::send(const UUri &uri,
                              const UPayload &payload,
                              const UAttributes &attributes) noexcept {
    UStatus status;

    return status;
}

UStatus DummyUTransport::registerListener(const UUri &uri,
                                          const UListener &listener) noexcept {

    UStatus status;

    return status;
}

UStatus DummyUTransport::unregisterListener(const UUri &uri,
                                            const UListener &listener) noexcept {

    UStatus status;

    return status;
}

UStatus DummyUTransport::receive(const UUri &uri,
                                 const UPayload &payload,
                                 const UAttributes &attributes) noexcept {

    UStatus status;

    (void)uri;
    (void)payload;
    (void)attributes;

    spdlog::error("not implemented");

    status.set_code(UCode::UNAVAILABLE);

    return status;
}